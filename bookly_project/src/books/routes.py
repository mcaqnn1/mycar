from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from books.books_data import Books
from books.schemas import BooksModel,BookUpdateModel

router = APIRouter()

@router.get("/")
async def get_all_books() -> list:
    return Books

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=BooksModel)
async def create_book(book: BooksModel) -> dict:
    new_book = book.model_dump()
    Books.append(new_book)
    return new_book

@router.get("/{book_id}/",response_model=BooksModel)
async def get_book(book_id: int):
    for book in Books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found"
    )
        
@router.put("/{book_id}/",status_code=status.HTTP_200_OK,response_model=BooksModel)
async def update_book(book_id: int,book_update: BookUpdateModel):
    for book in Books:
        if book['id'] == book_id:
            book['id'] = book_update.id
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['published_date'] = book_update.published_date
            book['page_count'] = book_update.page_count
            book['language'] = book_update.language
            return book
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND, 
        detail = "Book not found"
    )

@router.delete("/{book_id}/",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in Books:
        if book['id'] == book_id:
            Books.remove(book)
            return
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND, 
        detail = "Book not found"
    )
