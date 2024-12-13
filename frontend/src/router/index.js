import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';
import Doctors from "../views/Doctors.vue";
import About from "../views/About.vue";
import Contact from "../views/Contact.vue";
import Doctor_details from "../views/Doctor_details.vue";
// import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/Rigister.vue';


const routes = [
  // { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/doctors",
    name: "Doctors",
    component: Doctors,
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
    path: "/doctor-details",
    name: "Doctor_details",
    component: Doctor_details,
  },
  ...authRoutes,
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory(),
  routes,
});

export default router;
