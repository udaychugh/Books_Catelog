import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import 'font-awesome/css/font-awesome.min.css';
import '../node_modules/font-awesome/css/font-awesome.min.css'; 


function App() {
  const [books, setBooks] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [genreFilter, setGenreFilter] = useState('all');
  const [minPriceFilter, setMinPriceFilter] = useState('');
  const [maxPriceFilter, setMaxPriceFilter] = useState('');

  useEffect(() => {
    // Fetch all books on component mount
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    const response = await fetch('/books');
    const data = await response.json();
    setBooks(data);
  };

  const searchBooks = async () => {
    const response = await fetch(`/books/search?query=${searchQuery}`);
    const data = await response.json();
    setBooks(data);
  };

  const filterBooks = async () => {
    
    const response = await fetch(`/books/filter?genre=${genreFilter}&min_price=${minPriceFilter}&max_price=${maxPriceFilter}`);
    const data = await response.json();
    setBooks(data);
  };
  

  

  return (
    <div className='mainHeader'>
      
      <div className='bookstore_navbar'>
        <h1>Online Bookstore</h1>
        <div className='searchBar'>
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            
            placeholder="Search books"
          />
          <button onClick={searchBooks}>Search</button>
        </div>
      </div>

      <div className='filterClass'>
        <select value={genreFilter} onChange={(e) => setGenreFilter(e.target.value)}>
          <option value="all">All Genres</option>
          <option value="fiction">Fiction</option>
          <option value="non-fiction">Non-Fiction</option>
          <option value="science-fiction">Science Fiction</option>
          <option value="fantasy">Fantasy</option>
          {/* Add more genre options */}
        </select>

        <input
          type="number"
          value={minPriceFilter}
          onChange={(e) => setMinPriceFilter(e.target.value)}
          placeholder="Min Price"
        />

        <input
          type="number"
          value={maxPriceFilter}
          onChange={(e) => setMaxPriceFilter(e.target.value)}
          placeholder="Max Price"
        />

        <button className='btnBuy' onClick={filterBooks}>Filter</button>
      </div>

      <div className='dothemincenter'>
        {books.map((book) => (
          <div className='showingBooks' key={book.id}>
            <img src={book.cover_image} alt={book.title} />
            <div className='detailstab'>
              <h2>{book.title}</h2>
              <p>Author : {book.author}</p>
              <p>Description : {book.description}</p>
              <p>Genre : {book.genre}</p>
              <p>Price : &#8377;{book.price}</p>
              <p>Publication Date : {book.publication_date}</p>
              <p>Rating : {book.rating}</p>
            </div>
            <button className='btnBuy'>Buy Now</button>
            <br></br>
            <br></br>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
