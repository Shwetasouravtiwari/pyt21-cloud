import axios from 'axios'
import React, { useState } from 'react'

const AddProductForm = () => {
    const [name, setName] = useState('')
    const [description, setDescription] = useState('')
    const [categoryId, setCategoryId] = useState(1)

    const handleSubmit = async e => {
        e.preventDefault()
        await axios.post('https://pyt21-webapi.azurewebsites.net/api/products', { name, description, categoryId })

        setName('')
        setDescription('')
        setCategoryId(1)
    }

    return (
        <div className="container col-md-6 my-5">
            <div className="card">
                <div className="card-body">
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label className="form-label">Product Name</label>
                            <input value={name} onChange={e => setName(e.target.value)} type="text" className="form-control" />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Description</label>
                            <input value={description} onChange={e => setDescription(e.target.value)} type="text" className="form-control" />
                        </div>
                        <button type="submit" className="btn btn-secondary">Create Product Now</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default AddProductForm
