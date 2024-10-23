import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<ProductList />} />
                    <Route path="/products/:id" element={<ProductDetail />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
