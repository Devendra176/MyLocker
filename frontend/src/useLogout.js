import { useState } from 'react';

export default function useLogout() {
    const deleteToken = () => {
        const tokenString = localStorage.setItem('Authorization', null);
        const authenticated = localStorage.setItem('authenticated', false);
        const data = {
            'token': tokenString,
            'authenticated': authenticated
        }
        return data
    };
    const [token, setToken] = useState(deleteToken());
    const [authenticated, setAuthenticated] = useState(deleteToken());

  return {
    authenticated: authenticated,
    token
  }
}
