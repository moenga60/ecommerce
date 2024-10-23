import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getProducts = async () => {
    return await axios.get(`${API_URL}/products/`);
};

export const getProductDetail = async (id) => {
    return await axios.get(`${API_URL}/products/${id}/`);
};
