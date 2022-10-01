import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { NavLink } from 'react-router-dom';
import useToken from '../useToken';

function NavBarComponent() {
  const { token, setToken } = useToken();
  return (
    <>
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand as={NavLink} to="/">MyLocker</Navbar.Brand>
          <Nav className="me-auto">
            {/* <Nav.Link as={NavLink} to="/home">Home</Nav.Link> */}
          </Nav>
          <Nav>
          <Nav.Link className='justify-content-end' as={NavLink} to={token.authenticated === 'true' ? "/logout": "/login"}>{token.authenticated === 'true' ? "Logout": "Login"}</Nav.Link>
          {token.authenticated ==='false' ? <Nav.Link as={NavLink} to="/about">About</Nav.Link>: undefined}
          {token.authenticated ==='false' ? <Nav.Link as={NavLink} to="/contact">Contact Us</Nav.Link>: undefined}
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default NavBarComponent;