<template>
  <div class="h-screen  bg-gradient-to-t from-sky-200 to-white  flex items-center justify-center px-4">
    <div class="bg-white shadow-md rounded-lg p-8 max-w-sm w-full">
      <h2 class="text-2xl font-extrabold   text-gray-600 ">Login</h2>
      <p class="text-sm font-normal text-gray-500 py-4"> Please log in to book appointment </p>
      <form @submit.prevent="handleLogin">

        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Email</label>
          <input v-model="email" type="email" class="border rounded px-4 py-2 w-full outline-none" />
        </div>

        <div class="mb-4">
          <label for="password" class="text-sm font-medium mb-1">Password</label>
          <input type="password" id="password" v-model="password" class="border rounded px-4 py-2 w-full outline-none"
            placeholder="Enter your password" required />
        </div>

        <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition">
          Login
        </button>
        
        <p class="text-sm font-medium pt-2 text-gray-600">Create an new account ?
          <router-link to="/register" class="cursor-pointer text-blue-500">
            Click here
          </router-link>
        </p>
      </form>

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
