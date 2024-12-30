// src/auth.js
import { ref } from "vue";

export const isLoggedIn = ref(!!sessionStorage.getItem("user"));

export const login = (userData) => {
  const user = {
    name: userData.name,
    user_image: userData.user_image,
    full_name: userData.full_name,
  };

  console.log("User Object during Login:", user);  
  sessionStorage.setItem("user", JSON.stringify(user));
  isLoggedIn.value = true;
};


export const logout = () => {
  sessionStorage.removeItem("user");
  isLoggedIn.value = false;
};
