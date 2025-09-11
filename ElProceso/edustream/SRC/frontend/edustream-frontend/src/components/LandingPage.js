import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import Carousel from 'react-bootstrap/Carousel';
import Card from 'react-bootstrap/Card';


function ColorSchemesExample() {
    return (
        <div style={{
            background: "linear-gradient(135deg, #f8fafc 0%, #e3e8ee 100%)",
            minHeight: "100vh"
        }}>
            <Navbar expand="xxl" bg="dark" data-bs-theme="dark" className='px-3 shadow-sm'>
                <Container>
                    <Navbar.Brand href="#home" className='fs-3' style={{ fontFamily: 'Figtree' }}>
                        Edu<span className="text-primary" style={{ fontFamily: 'Instrument Serif, serif' }}>Stream</span>
                    </Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
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
            <Container style={{ marginTop: '40px', fontFamily: 'Figtree, Barlow' }}>
                <Row className="justify-content-center align-items-center" style={{ minHeight: '30vh' }}>
                    <Col md={8} className="text-center">
                        <h1 style={{ fontFamily: 'initial', fontWeight: 700, fontSize: '2.5rem' }}>Bienvenido a EduStream</h1>
                        <p style={{ fontSize: '1.2rem', color: '#333' }}>
                            Tu solución integral para la educación en línea.<br />
                            <span style={{ color: "#0d6efd", fontWeight: "bold" }}>
                                Aprende, crece y destaca en tu carrera.
                            </span>
                        </p>
                    </Col>
                </Row>
                <Row className="justify-content-center align-items-center">
                    <Col md={6}>
                        <form>
                            <InputGroup className="mb-4">
                                <Form.Control
                                    placeholder="Ingresa tu email"
                                    aria-label="Email"
                                    aria-describedby="basic-addon2"
                                />
                                <Button variant="outline-primary" id="button-addon2">
                                    Comenzar
                                </Button>
                            </InputGroup>
                        </form>
                    </Col>
                </Row>
            </Container>
            <Container className="mt-4">
                <Carousel>
                    <Carousel.Item>
                        <img src="https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=800&q=80" alt="Curso 1" className="d-block w-100" style={{ maxHeight: "300px", objectFit: "cover" }} />
                        <Carousel.Caption>
                            <h3>Programación Web</h3>
                            <p>Domina HTML, CSS y JavaScript desde cero.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=800&q=80" alt="Curso 2" className="d-block w-100" style={{ maxHeight: "300px", objectFit: "cover" }} />
                        <Carousel.Caption>
                            <h3>Data Science</h3>
                            <p>Aprende análisis de datos y Python.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img src="https://images.unsplash.com/photo-1503676382389-4809596d5290?auto=format&fit=crop&w=800&q=80" alt="Curso 3" className="d-block w-100" style={{ maxHeight: "300px", objectFit: "cover" }} />
                        <Carousel.Caption>
                            <h3>Diseño Gráfico</h3>
                            <p>Crea proyectos visuales impactantes.</p>
                        </Carousel.Caption>
                    </Carousel.Item>
                </Carousel>
                <Row className="mt-4">
                    <Col md={4} className="mb-3">
                        <Card className="shadow-sm h-100">
                            <Card.Img variant="top" src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=400&q=80" />
                            <Card.Body>
                                <Card.Title>Curso de React</Card.Title>
                                <Card.Text>Categoría: Programación</Card.Text>
                                <Button variant="primary" size="sm">Ver más</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4} className="mb-3">
                        <Card className="shadow-sm h-100">
                            <Card.Img variant="top" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=400&q=80" />
                            <Card.Body>
                                <Card.Title>Curso de Python</Card.Title>
                                <Card.Text>Categoría: Data Science</Card.Text>
                                <Button variant="primary" size="sm">Ver más</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={4} className="mb-3">
                        <Card className="shadow-sm h-100">
                            <Card.Img variant="top" src="https://images.unsplash.com/photo-1503676382389-4809596d5290?auto=format&fit=crop&w=400&q=80" />
                            <Card.Body>
                                <Card.Title>Curso de Diseño</Card.Title>
                                <Card.Text>Categoría: Creatividad</Card.Text>
                                <Button variant="primary" size="sm">Ver más</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
            <Container>
                <Form className="mt-4">
                    <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="name@example.com" />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                        <Form.Label>Example textarea</Form.Label>
                        <Form.Control as="textarea" rows={3} />
                    </Form.Group>
                </Form>
            </Container>
            <footer className="text-center mt-5 mb-3" style={{ color: "#555" }}>
                <small>© 2025 EduStream Pro. Todos los derechos reservados.</small>
            </footer>
        </div>
    );
}

export default ColorSchemesExample;