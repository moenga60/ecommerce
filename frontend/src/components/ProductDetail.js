import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getProductDetail } from '../services/api';
import '../ProductDetail.css'; 


const ProductDetail = ({ onClose }) => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        const fetchProductDetail = async () => {
            try {
                const response = await getProductDetail(id);
                setProduct(response.data);
            } catch (error) {
                console.error('Error fetching product detail:', error);
            }
        };

        fetchProductDetail();
    }, [id]);

    if (!product) return <p>Loading...</p>;

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <button className="close-button" onClick={onClose}>×</button>
                <div className="product-details">
                    <img className="product-image" src={`http://localhost:8000${product.imageUrl}`} alt={product.name} />
                    <h2>{product.name}</h2>
                    <p>{product.description}</p>
                    <p><strong>Price:</strong> Ksh {product.price}</p>
                    <p><strong>Stock:</strong> {product.stock}</p>
                </div>
            </div>
        </div>
    );
};

export default ProductDetail;
