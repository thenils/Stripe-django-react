import React from 'react';
import './App.css';
import {
    Elements,
} from '@stripe/react-stripe-js';

import { loadStripe } from "@stripe/stripe-js/pure";
import CheckoutForm from "./components/CheckoutForm";

const stripePromise = loadStripe('pk_test1_51J5RXzSIyKBcYOPsQ2H6cqLwes6RoffzLAys9V7c0daeCOb4Q2MtNLct4EQEQQY3f8IXzvZD1PxLbvqpSspUeAFn00uALQbf2v');


const App = () => ( <
    Elements stripe = { stripePromise } >
    <
    CheckoutForm / >
    <
    /Elements>
);

export default App;
