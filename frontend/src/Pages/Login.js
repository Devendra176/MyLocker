import React, { useState } from 'react';

import './Css/login.css';

export const LoginPage = (props)=> {
    const [phone, setPhone] = useState("");
    const [otp, setOtp] = useState("");
    const [is_valid_phone, set_is_valid_phone] = useState(0);
    const [authenticated, setauthenticated] = useState(localStorage.getItem(localStorage.getItem("authenticated")|| false));
    const [message_phone, setMessagePhone] = useState({});
    const [message_otp, setMessageOtp] = useState({});
    const submit = (e) => {
      e.preventDefault();
      if (!phone){
          alert('Empty Field');
      }
      else{
            if (!is_valid_phone){
                props.phoneRegister(phone, set_is_valid_phone);
                setPhone(phone);
            }else if(is_valid_phone){
                props.verifyNumber(phone, otp, setauthenticated);
            }
            
      }
    }
  return (
    <>
        <section className="vh-100">
        <div className="container py-5 h-100">
            <div className="row d-flex align-items-center justify-content-center h-100">
            <div className="col-md-8 col-lg-7 col-xl-6">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg"
                className="img-fluid" alt="Phone"/>
            </div>
            <div className="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
                <form onSubmit={submit}>

                <div className="form-outline mb-4">
                    <label className="form-label" htmlFor="phone">Enter your mobile number</label>
                    <input type="text" id="phone" value={phone} onChange={(e)=>setPhone(e.target.value)} className="form-control form-control-lg" />
                </div>
                <div className="form-outline mb-4" style={is_valid_phone ? {display: 'block'}: {display: 'none'} }>
                    <label className="form-label" htmlFor="otp">Enter OTP</label>
                    <input type="text" id="otp" value={otp} onChange={(e)=>setOtp(e.target.value)} className="form-control form-control-lg" />
                </div>
                <button type="submit" className="btn btn-primary btn-lg btn-block">send OTP</button>
                </form>
            </div>
            </div>
        </div>
        </section>
    </>
  );
}