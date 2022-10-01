import { useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import useLogout  from '../useLogout';

export default function Logout() {
    const { token, setToken } = useLogout();
    const navigate = useNavigate();
    useEffect(() => {
        if (token.authenticated === 'false'){
         navigate("/login");   
        }
    },[])
}
