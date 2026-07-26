async function buscarLivro() {

    const isbn = document.getElementById("isbn").value;

    const response = await fetch(`/books/search/${isbn}`);

    if (!response.ok) {
        alert("Livro não encontrado!");
        return;
    }

    const book = await response.json();

    document.getElementById("title").value = book.title;
    document.getElementById("author").value = book.author;
    document.getElementById("category").value = book.category;

    const cover = document.getElementById("book-cover");

    if (book.thumbnail) {
        cover.src = book.thumbnail;
        cover.style.display = "block";
    }

}