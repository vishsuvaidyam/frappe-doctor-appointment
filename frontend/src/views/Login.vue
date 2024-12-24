<template>
  <div class="h-screen  bg-gradient-to-t from-sky-200 to-white  flex items-center justify-center px-4">
    <div class="bg-white shadow-md rounded-lg p-8 max-w-sm w-full">
      <h2 class="text-2xl font-extrabold   text-gray-600 ">Login</h2>
      <p class="text-sm font-normal text-gray-500 py-4"> Please log in to book appointment </p>
      <form @submit.prevent="handleLogin">

        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Email</label>
          <div class="mb-4">
                    <div class="relative">
                        <i
                            class="fa-solid fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                        <input v-model="email" type="email"
                            class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                            placeholder="Email" />
                    </div>
                </div>
        </div>
        

        <div class="mb-4">
          <label for="password" class="text-sm font-medium mb-1">Password</label>
           <div class="mb-4">
                    <div class="relative">
                        <i
                            class="fa-solid fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                        <input v-model="password" type="password"
                            class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                            placeholder="Password" />
                    </div>
                </div>
        </div>

        <button type="submit" class="w-full bg-black text-white py-3 rounded-lg text-sm font-semibold hover:bg-gray-800">
          Login
        </button>

        <p class="text-sm font-medium pt-2 text-gray-600">Create an new account ?
          <router-link to="/register" class="cursor-pointer text-blue-500">
            Click here
          </router-link>
        </p>
      </form>
      <div class="flex gap-4 pt-4 w-auto justify-center">
        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
          <img src="https://www.google.com/favicon.ico" alt="Google" class="w-6 h-6">
        </button>

        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
          <img src="https://www.facebook.com/favicon.ico" alt="Facebook" class="w-6 h-6">
        </button>

        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
          <img src="https://www.apple.com/favicon.ico" alt="Apple" class="w-6 h-6">
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: null,
      password: null,
    };
  },
  inject: ["$auth"],
  async mounted() {
    if (this.$route?.query?.route) {
      this.redirect_route = this.$route.query.route;
      this.$router.replace({ query: null });
    }
  },
  methods: {
    async login() {
      if (this.email && this.password) {
        let res = await this.$auth.login(this.email, this.password);
        if (res) {
          this.$router.push({ name: "Navbar" });
        }
      }
    },
  },
};
</script>
