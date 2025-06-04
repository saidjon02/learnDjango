from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# frontend reactda app.jsx fayliga buni yozamiz:

# import React, { useEffect, useState } from 'react';
# function App() {
#   const [products, setProducts] = useState([]);
#   const [form, setForm] = useState({ name: '', price: '' });

#   useEffect(() => {
#     fetch('http://localhost:8000/api/products/')
#       .then(res => res.json())
#       .then(data => setProducts(data));
#   }, []);

#   const handleSubmit = (e) => {
#     e.preventDefault();
#     fetch('http://localhost:8000/api/products/', {
#       method: 'POST',
#       headers: { 'Content-Type': 'application/json' },
#       body: JSON.stringify(form)
#     })
#       .then(res => res.json())
#       .then(data => setProducts([...products, data]));
#   };

#   const handleDelete = (id) => {
#     fetch(`http://localhost:8000/api/products/${id}/`, {
#       method: 'DELETE'
#     }).then(() => setProducts(products.filter(p => p.id !== id)));
#   };

#   return (
#     <div>
#       <h1>Mahsulotlar</h1>
#       <form onSubmit={handleSubmit}>
#         <input
#           type="text"
#           placeholder="Nomi"
#           value={form.name}
#           onChange={e => setForm({ ...form, name: e.target.value })}
#         />
#         <input
#           type="number"
#           placeholder="Narxi"
#           value={form.price}
#           onChange={e => setForm({ ...form, price: e.target.value })}
#         />
#         <button type="submit">Qo'shish</button>
#       </form>
#       <ul>
#         {products.map(p => (
#           <li key={p.id}>
#             {p.name} - {p.price} so'm
#             <button onClick={() => handleDelete(p.id)}>❌</button>
#           </li>
#         ))}
#       </ul>
#     </div>
#   );
# }

# export default App;
