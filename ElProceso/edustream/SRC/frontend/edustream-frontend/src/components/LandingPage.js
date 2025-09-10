import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';


function ColorSchemesExample() {
    return (
        <>
            <Navbar expand="xxl" bg="dark" data-bs-theme="dark" className='px-3 shadow-sm'>
                <Container>
                    <Navbar.Brand href="#home" className='fs-3' style={{ fontFamily: 'Figtree' }}>Edu<span className="text-primary" style={{ fontFamily: 'Instrument Serif, serif' }}>Stream</span></Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#cursos">Cursos</Nav.Link>
                        <Nav.Link href="#about">About</Nav.Link>
                    </Nav>
                </Container>
                <Row>
                    <Col xs="auto">
                        <Button variant='light' type="submit">Login</Button>
                    </Col>
                    <Col xs="auto">
                        <Button variant='primary' type="submit" className='ms-1'>Register</Button>
                    </Col>
                </Row>
            </Navbar>
            <br />
            <Container style={{ minHeight: '60vh', marginTop: '40px', fontFamily: 'Figtree, Barlow' }}>
                <Row className="justify-content-center align-items-center" style={{ minHeight: '40vh' }}>
                    <Col md={6} className="d-flex align-items-center justify-content-center">
                        <div>
                            <h1 style={{ fontFamily: 'initial' }}>Bienvenido a EduStream</h1>
                            <p>Tu solución integral para la educación en línea.</p>
                        </div>
                    </Col>
                </Row>
            </Container>
            <Container>
                <form>
                    <Row className="justify-content-center align-items-center">
                        <Col md={6}>
                            <InputGroup className="mb-3">
                                <Form.Control
                                    placeholder="Email"
                                    aria-label="Recipient's username"
                                    aria-describedby="basic-addon2"
                                />
                                <Button variant="outline-secondary" id="button-addon2">
                                    Comenzar
                                </Button>
                            </InputGroup>
                        </Col>
                    </Row>
                </form>
            </Container>
        </>
    );
}


export default ColorSchemesExample;