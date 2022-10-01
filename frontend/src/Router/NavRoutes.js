import React, {useEffect, useState} from 'react';
import {Routes, Route } from "react-router-dom";
import AboutPage from '../Pages/About';
import ContactPage from '../Pages/Contact';

import {LoginPage} from '../Pages/Login';
import {Profile} from '../Pages/Dashboard';

import { phoneRegister, verifyNumber } from '../Functions/login_function';
import useToken from '../useToken';
import Logout from '../Pages/Logout';

export const NavPath = () => {
  const { token, setToken } = useToken();

  return (
    <>
        <Routes>
            <Route path="about" element={token.authenticated === 'true' ? <Profile /> : <AboutPage />}></Route>
            <Route path="contact" element={token.authenticated === 'true' ? <Profile /> : <ContactPage />}></Route>
            <Route path="login" element={token.authenticated === 'true' ? <Profile /> : <LoginPage phoneRegister={phoneRegister} verifyNumber={verifyNumber} />}></Route>
            <Route path="logout" element={<Logout />}></Route>
        </Routes>
    </>
  );
}

