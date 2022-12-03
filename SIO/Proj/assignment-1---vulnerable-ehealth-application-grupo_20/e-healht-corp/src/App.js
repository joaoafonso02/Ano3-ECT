import './App.css';
import { MyNavbar } from './components/MyNavbar';
import { Home, Contacts, Appointments, Tests, Login} from './pages';

// import { Button, Container, Row, Col } from 'react-bootstrap';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  
  return (
    <>
      <BrowserRouter>
        <MyNavbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="contacts" element={<Contacts />} />
          <Route path="/appointments" element={<Appointments />} />
          <Route path="/tests" element={<Tests />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
