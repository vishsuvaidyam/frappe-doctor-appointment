import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';
import Doctors from "../views/Doctors.vue";
import About from "../views/About.vue";
import Contact from "../views/Contact.vue";
import Doctor_details from "../views/Doctor_details.vue";
import RegisterPage from '@/views/Register.vue';
import Profile from "../components/Profile.vue";
import LoginPage from '../components/Login.vue';
import Test from "../views/test.vue";
 


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
    path: "/doctor-details/:full_name",
    name: "Doctor_details",
    component: Doctor_details,
  },

  {
    path:"/profile",
    name:"Profile",
    component:Profile,
  },
  {
    path:"/test",
    name:"Test",
    component:Test,
  },
  {
    path:"/loginPage",
    name:"LoginPage",
    component:LoginPage,
  },

  ...authRoutes,
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory(),
  routes,
});

export default router;
