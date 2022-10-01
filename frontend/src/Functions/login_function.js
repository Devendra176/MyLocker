 export const phoneRegister = (phone, set_is_valid_phone) => {
    const mobileDetail = {
        phone: phone,
    }
    register(mobileDetail, set_is_valid_phone);
}

const register = async (mobileDetail, set_is_valid_phone)=>{
    await fetch('phone/register/', {
       method: 'POST',
       body: JSON.stringify({
            phone: mobileDetail.phone
       }),
       headers: {
          'Content-type': 'application/json; charset=UTF-8',
       },
    })
       .then((response) => response.json())
       .then((data) => {
        if (data.is_valid){
         set_is_valid_phone(1);
        }else{
         console.log(data.errors)
        }
        console.log(data);
       })
       .catch((err) => {
          console.log(err.message);
       });
}

export const verifyNumber = (phone, otp, setauthenticated) => {
    const otpDetail = {
        phone: phone,
        otp: otp,
    }
    verify(otpDetail, setauthenticated);
}
const verify = async (otpDetail, setauthenticated)=>{
    await fetch('phone/verification/', {
       method: 'POST',
       body: JSON.stringify({
            phone: otpDetail.phone,
            otp: otpDetail.otp,
       }),
       headers: {
          'Content-type': 'application/json; charset=UTF-8',
       },
    })
       .then((response) => response.json())
       .then((data) => {
        console.log(data);
        if (data.is_valid){
         setauthenticated(data.is_valid)
         localStorage.setItem("authenticated", true);
         localStorage.setItem("Authorization", "token "+ data.token);
         // window.location.href = "/";
        }

       })
       .catch((err) => {
          console.log(err.message);
       });
}