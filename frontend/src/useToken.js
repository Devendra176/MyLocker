import { useState } from 'react';

export default function useToken() {
  const getToken = () => {
    const tokenString = localStorage.getItem('Authorization');
    const authenticated = localStorage.getItem('authenticated');
    const data = {
        'token': tokenString,
        'authenticated': authenticated
    }
    return data
  };
  const [token, setToken] = useState(getToken());
  const [authenticated, setAuthenticated] = useState(getToken());
  return {
    authenticated: authenticated,
    token
}
}