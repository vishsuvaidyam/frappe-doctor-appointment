<template>
 <div class="h-screen bg-gray-100 flex items-center justify-center px-4">
    <!-- Login Card -->
    <div class="bg-white shadow-md rounded-lg p-8 max-w-sm w-full">
      <h2 class="text-2xl font-semibold text-center text-gray-700 mb-6">Login</h2>
      <form @submit.prevent="handleLogin">
        <!-- Email Input -->
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            class="mt-1 block w-full border-gray-300 rounded-2 px-4 py-2 shadow-sm focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter your email"
            required
          />
        </div>

        <!-- Password Input -->
        <div class="mb-4">
          <label for="password" class="block text-sm  font-medium text-gray-700">Password</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="mt-1 block w-full border-gray-300 rounded-2 px-4 py-2 shadow-sm focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter your password"
            required
          />
        </div>

        <!-- Login Button -->
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition">
          Login
        </button>
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
