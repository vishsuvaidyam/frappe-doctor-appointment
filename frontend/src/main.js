import "./style.css"
import { createApp, reactive } from "vue";
import App from "./App.vue";

import router from './router';
import resourceManager from "../../../doppio/libs/resourceManager";
import call from "../../../doppio/libs/controllers/call";
import socket from "../../../doppio/libs/controllers/socket";
import Auth from "../../../doppio/libs/controllers/auth";
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const options = {
  position: "top-right",
  timeout: 3000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
};

const app = createApp(App);
const auth = reactive(new Auth());

// Plugins
app.use(router);
app.use(resourceManager);

// Global Properties,
// components can inject this
app.provide("$auth", auth);
app.provide("$call", call);
app.provide("$socket", socket);


// Configure route gaurds
// router.beforeEach(async (to, from, next) => {
// 	if (to.matched.some((record) => !record.meta.isLoginPage)) {
// 		if (!auth.isLoggedIn) {
// 			next({ name: 'Login', query: { route: to.path } });
// 		} else {
// 			next();
// 		}
// 	} else {
// 		if (auth.isLoggedIn) {
// 			next({ name: 'Home' });
// 		} else {
// 			next();
// 		}
// 	}
// });
app.use(Toast, options);
app.mount("#app");
