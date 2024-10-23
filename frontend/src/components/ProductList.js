import React, { useState, useEffect } from 'react';
import { getProducts } from '../services/api';
import { Link } from 'react-router-dom';
import '../ProductList.css'; 

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        fetchProducts();
    },[]);

    const fetchProducts = async () => {
        try {
            const response = await getProducts();
            console.log(response)
            setProducts(response.data);
        } catch (error) {
            console.error('Error fetching products:', error);
        }
    };

    const handleSearchChange = (e) => {
        setSearchTerm(e.target.value);
    };

    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div>
            {/* Navigation Bar */}
            <nav className="navbar">
                <div className="logo">
                    <h2>DickiesStore</h2>
                </div>
                <ul className="menu">
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/products">Products</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                </ul>
                <div className="nav-right">
                    <input 
                        type="text" 
                        placeholder="Search products..." 
                        value={searchTerm}
                        onChange={handleSearchChange} 
                        className="search-bar"
                    />
                    <Link to="/cart" className="cart-icon">🛒 Cart</Link>
                    <Link to="/login" className="login-btn">Login</Link>
                </div>
            </nav>

            {/* Product List */}
            <div className="product-container">
                {filteredProducts.length > 0 ? (
                    filteredProducts.map((product) => (
                        <div key={product.id} className="product-card">
                            <img src={product.image} alt={product.name} className="product-image" />
                            <h3>{product.name}</h3>
                            <p className="product-price">Price: Ksh {product.price}</p>
                            <Link to={`/products/${product.id}`} className="view-details-btn">View Details</Link>
                        </div>
                    ))
                ) : (
                    <p>No products found.</p>
                )}
            </div>
        </div>
    );
};

export default ProductList;
