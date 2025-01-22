// src/auth.js
import { ref } from "vue";
// import { useRouter } from "vue-router";

// const router=useRouter();
export const isLoggedIn = ref(!!sessionStorage.getItem("user") || !!localStorage.getItem("user"));

export const login = (userData) => {
  const user = {
    name: userData.name,
    user_image: userData.user_image,
    full_name: userData.full_name,
  };

  console.log("User Object during Login:", user);  
  sessionStorage.setItem("user", JSON.stringify(user));
  localStorage.setItem("user", JSON.stringify(user));
  isLoggedIn.value = true;
  console.log(isLoggedIn.value );
  // router.push('/')
};


export const logout = () => {
  sessionStorage.removeItem("user");
  localStorage.removeItem("user");
  isLoggedIn.value = false;
};



