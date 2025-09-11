import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';



function Login() {
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
                <h2 className="mb-4 text-center">Iniciar Sesión</h2>
                <Form>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" />
                        <Form.Text className="text-muted">
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicCheckbox">
                        <Form.Check type="checkbox" label="Check me out" />
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>
            </Container>
            <footer className="text-center mt-5 mb-3" style={{ color: "#555" }}>
                <small>© 2025 EduStream Pro. Todos los derechos reservados.</small>
            </footer>
        </div>
    );
}

export default Login;