async function buscarLivro() {

    const isbn = document.getElementById("isbn").value;

    const response = await fetch(`/books/search/${isbn}`);

    if (!response.ok) {
        alert("Livro não encontrado!");
        return;
    }

    const book = await response.json();
    const cover = document.getElementById("book-cover");

    cover.src = `https://covers.openlibrary.org/b/isbn/${isbn}-L.jpg`;
    cover.style.display = "block";

    document.getElementById("title").value = book.title;
    document.getElementById("author").value = book.author;
    document.getElementById("category").value = book.category;

}