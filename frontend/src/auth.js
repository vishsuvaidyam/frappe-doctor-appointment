// src/auth.js
import { ref } from "vue";

export const isLoggedIn = ref(!!sessionStorage.getItem("user"));

export const login = (user) => {
  sessionStorage.setItem("user", JSON.stringify(user));
  isLoggedIn.value = true;
};

export const logout = () => {
  sessionStorage.removeItem("user");
  isLoggedIn.value = false;
};
