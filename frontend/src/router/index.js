import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';
import Doctors from "../views/Doctors.vue";
import About from "../views/About.vue";
import Contact from "../views/Contact.vue";
import Doctor_details from "../views/Doctor_details.vue";
import RegisterPage from '@/views/Register.vue';
import Profile from "../components/Profile.vue";
import LoginPage from '../views/Login.vue';
import My_appointments from "../components/My_appointments.vue";
import NotFound from "../views/NotFound.vue";
import Doctor_appointment from "../views/Doctor_appointment.vue";
import Patient_details from "../components/Patient_details.vue";
import Payment from "../components/Payment.vue";

const routes = [
  { path: '/register', 
    component: RegisterPage,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/doctors",
    name: "Doctors",
    component: Doctors,
    props: true
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: '/doctor-details/:full_name/:specialist?',
    name: "Doctor_details",
    component: Doctor_details,
  },

  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/loginPage",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/my-appointment",
    name: "My_appointments",
    component: My_appointments,
  },
  {
    path: "/patient/:full_name/:specialist/:formattedDateTime",
    name: "Patient_details",
    component: Patient_details,
  },
  {
    path: "/payment",
    name: "Payment",
    component: Payment,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: NotFound,
  }, 
  {
    path: "/doctor-appointment",
    name: "Doctor_appointment",
    component: Doctor_appointment,
  },

  ...authRoutes,
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory(),
  routes,
});

export default router;
