/* eslint-disable no-console */
/* eslint-disable react/prop-types */
import React from 'react';
import { Redirect } from 'react-router-dom';
import Joi from '@hapi/joi';
import axios from 'axios';
import RegisterFormPresentation from './RegisterFormPresentation';

const RegisterForm = (props) => {
  const { email, role, registertoken } = props;
  console.log(email);
  const [values, setValues] = React.useState({
    registertoken,
    email,
    firstName: '',
    lastName: '',
    password: '',
    rePassword: '',
    showPassword: false,
    errorMessage: '',
    role,
    redirect: false,
  });


  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const changeErrorMessage = (message) => {
    setValues({ ...values, errorMessage: message });
  };

  const schema = Joi.object({

    email: Joi.string()
      .email({ minDomainSegments: 2, tlds: { allow: false } }),

    firstName: Joi.string()
      .alphanum()
      .min(3)
      .max(50)
      .required(),

    lastName: Joi.string()
      .alphanum()
      .min(3)
      .max(50)
      .required(),

    password: Joi.string()
      .pattern(new RegExp('^[a-zA-Z0-9]{3,30}$')),

    rePassword: Joi.ref('password'),

    showPassword: Joi.any(),

    errorMessage: Joi.any(),

    registertoken: Joi.any(),

    role: Joi.any(),

    redirect: Joi.boolean(),
  });

  const validation = async (ip) => {
    let validationSuccess = true;
    try {
      await schema.validateAsync(ip);
    } catch (err) {
      changeErrorMessage(err.message);
      validationSuccess = false;
    }
    return validationSuccess;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const validationSuccess = await validation(values);


    if (validationSuccess) {
      const registrationData = {
        token: values.registertoken, // should be taken by a token
        firstName: values.firstName,
        lastName: values.lastName,
        password: values.password,
      };

      await axios.post('http://localhost:8000/api/registration/register', registrationData)
        .then((res) => {
          console.log('Success: ', res);
          setValues({ ...values, redirect: true });
        })
        .catch((err) => {
          console.log('Axios error: ', err.message);
        });
    }
  };

  // if (values.redirect === 'notfound') {
  //   return <Redirect push to="" />;
  // }
  if (values.redirect === true) {
    return <Redirect push to="/login" />;
  }
  return (
    <div>
      <RegisterFormPresentation
        values={values}
        handleChange={handleChange}
        changeErrorMessage={changeErrorMessage}
        handleSubmit={handleSubmit}
      />
    </div>
  );
};

export default RegisterForm;
