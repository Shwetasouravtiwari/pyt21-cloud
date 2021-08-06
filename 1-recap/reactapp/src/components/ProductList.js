import React, {useState, useEffect} from 'react'
import axios from 'axios'

const ProductList = () => {
    const [products, setProducts] = useState([])

    async function fetchData() {
        const res = await axios.get('https://pyt21-webapi.azurewebsites.net/api/products')
        const data = await res.data
        setProducts(data)
    }

    useEffect(() => {
        fetchData()
    }, [products])

    return (
        <div className="container col-md-6 my-5">
            <ul className="list-group">
                {
                    products.map(product => (
                        <li className="list-group-item">#{product.id} {product.name} ({product.category}) - {product.description}</li>
                    ))
                }
            </ul>
        </div>
    )
}

export default ProductList
