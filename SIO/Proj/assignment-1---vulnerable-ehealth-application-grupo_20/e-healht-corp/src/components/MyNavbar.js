import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

export function MyNavbar() {
    return (
        <Navbar bg="light" expand="lg" style={{borderBottom: "1px solid #aaa"}}>
            <Container>
            <Navbar.Brand as={Link} to="/">eHealth Corp</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav" className='justify-content-end'>
                <Nav>
                    <Nav.Link as={Link} to="/contacts">Contacts</Nav.Link>
                    <Nav.Link as={Link} to="/appointments">Appointments</Nav.Link>
                    <Nav.Link as={Link} to="/tests">Tests</Nav.Link>
                    <Nav.Link as={Link} to="/login">Login</Nav.Link>
                </Nav>
            </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}