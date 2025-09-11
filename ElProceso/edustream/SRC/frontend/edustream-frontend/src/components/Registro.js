import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Alert from 'react-bootstrap/Alert';
import { registerUser } from '../modules/userModules';




function Registro() {
    const [form, setForm] = useState({
        username: '',
        email: '',
        password: '',
        password2: '',
        role: '',
        phone: ''
    });
    const [showAlert, setShowAlert] = useState(false);
    const [alertMsg, setAlertMsg] = useState('');
    const [alertVariant, setAlertVariant] = useState('success');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await registerUser(form);
        if (result.success) {
            setAlertMsg('Registro exitoso');
            setAlertVariant('success');
            setShowAlert(true);
            setTimeout(() => {
                setShowAlert(false);
                navigate('/login');
            }, 1800);
        } else {
            setAlertMsg(`Error: ${result.message}`);
            setAlertVariant('danger');
            setShowAlert(true);
        }
    };
    return (
        <div style={{
            background: "linear-gradient(135deg, #f8fafc 0%, #e3e8ee 100%)",
            minHeight: "100vh"
        }}>
            <Navbar expand="xxl" bg="dark" data-bs-theme="dark" className='px-3 shadow-sm'>
                <Container>
                    <Navbar.Brand href="/" className='fs-3' style={{ fontFamily: 'Figtree' }}>
                        Edu<span className="text-primary" style={{ fontFamily: 'Instrument Serif, serif' }}>Stream</span>
                    </Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="#cursos">Cursos</Nav.Link>
                        <Nav.Link href="#about">About</Nav.Link>
                    </Nav>
                    <Row>
                        <Col xs="auto">
                            <Button variant='light' type="submit" href='/login'>Login</Button>
                        </Col>
                        <Col xs="auto">
                            <Button variant='primary' type="submit" className='ms-1' href='/registro'>Register</Button>
                        </Col>
                    </Row>
                </Container>
            </Navbar>
            <Container className="d-flex flex-column justify-content-center align-items-center" style={{ minHeight: "80vh" }}>
            <Col md={6} lg={5} xl={4}>
                <h2 className="mb-4 text-center">Registro EduStream</h2>
                {showAlert && <Alert variant={alertVariant} onClose={() => setShowAlert(false)} dismissible>{alertMsg}</Alert>}
                <Form method='POST' onSubmit={handleSubmit}>
                    <Form.Group className="mb-3" controlId="formNombre">
                        <Form.Label>Nombre completo</Form.Label>
                        <Form.Control type="text" placeholder="Ingresa tu nombre completo" name="username" value={form.username} onChange={handleChange} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formEmail">
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="email" placeholder="Ingresa tu email" name="email" value={form.email} onChange={handleChange} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formPassword">
                        <Form.Label>Contraseña</Form.Label>
                        <Form.Control type="password" placeholder="Ingresa tu contraseña" name="password" value={form.password} onChange={handleChange} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formPassword2">
                        <Form.Label>Confirmar contraseña</Form.Label>
                        <Form.Control type="password" placeholder="Repite tu contraseña" name="password2" value={form.password2} onChange={handleChange} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formRol">
                        <Form.Label>Rol</Form.Label>
                        <Form.Select name="role" value={form.role} onChange={handleChange}>
                            <option value="">Selecciona tu rol</option>
                            <option value="estudiante">Estudiante</option>
                            <option value="profesor">Profesor</option>
                        </Form.Select>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formTelefono">
                        <Form.Label>Teléfono</Form.Label>
                        <Form.Control type="text" placeholder="Ingresa tu teléfono" name="phone" value={form.phone} onChange={handleChange} />
                    </Form.Group>
                    <Button variant="primary" type="submit" className="w-100">
                        Registrarse
                    </Button>
                </Form>
            </Col>
            </Container>
            <footer className="text-center mt-5 mb-3" style={{ color: "#555" }}>
                <small>© 2025 EduStream Pro. Todos los derechos reservados.</small>
            </footer>
        </div>
    );
}

export default Registro;