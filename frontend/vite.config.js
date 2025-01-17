import path from 'path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import proxyOptions from './proxyOptions';
import  Frappeui from 'frappe-ui/vite';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [vue(),Frappeui()],
	server: {
		port: 8080,
		proxy: proxyOptions
	},
	resolve: {
		alias: {
			'@': path.resolve(__dirname, 'src')
		}
	},
	build: {
		outDir: '../appointments_management/public/frontend',
		emptyOutDir: true,
		target: 'es2015',
        commonjsOptions: {
            include: [/tailwind.config.js/, /node_modules/],
        },
        sourcemap: true,
        rollupOptions: {
            output: {
                manualChunks: {
                    "frappe-ui": ["frappe-ui"],
                },
            },
        },
	},
	optimizeDeps: {
        include: [
            "frappe-ui > feather-icons",
            "showdown",
            "tailwind.config.js",
            "engine.io-client",
        ],
    },
});
