// Detectar si estamos en local o en producción
const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5000/api'
    : '/api';

// Cargar datos al iniciar
document.addEventListener('DOMContentLoaded', function() {
    cargarCustomers();
    
    // Event listener para botón actualizar
    document.getElementById('btnActualizar').addEventListener('click', cargarCustomers);
});

// Función para cargar customers
async function cargarCustomers() {
    try {
        document.getElementById('loadingDiv').style.display = 'block';
        document.getElementById('tableDiv').style.display = 'none';

        const response = await fetch(`${API_URL}/customers`);
        const result = await response.json();

        if (result.success) {
            mostrarCustomers(result.data);
            document.getElementById('totalCustomers').textContent = result.count;
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('No se pudo conectar con el servidor');
        console.error('Error:', error);
    } finally {
        document.getElementById('loadingDiv').style.display = 'none';
        document.getElementById('tableDiv').style.display = 'block';
    }
}

// Función para mostrar customers en la tabla
function mostrarCustomers(customers) {
    const tbody = document.getElementById('customersBody');
    tbody.innerHTML = '';

    customers.forEach(customer => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${customer.id}</td>
            <td>${customer.fullName}</td>
            <td>${customer.email}</td>
            <td><span class="tag is-info">${customer.type}</span></td>
            <td>${customer.discount}%</td>
            <td>$${customer.totalSale.toFixed(2)}</td>
        `;
        tbody.appendChild(tr);
    });
}
