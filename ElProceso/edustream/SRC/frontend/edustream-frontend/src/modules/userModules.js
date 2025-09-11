import axios from 'axios';


export async function registerUser(form) {
    if (form.password !== form.password2) {
        return { success: false, message: 'Las contraseñas no coinciden' };
    }
    try {
        const response = await axios.post('http://localhost:8000/api/usuarios/registro', {
            username: form.username,
            email: form.email,
            password: form.password,
            role: form.role,
            phone: form.phone
        });
        return { success: true, data: response.data };
    } catch (error) {
        return { success: false, message: 'Error en el registro', error };
    }
}
