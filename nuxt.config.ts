// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxtjs/supabase"],
  css: ['~/assets/css/main.css'],
  compatibilityDate: "2024-09-07",
  supabase: {
    login: '/login',
    callback: '/confirm',
    redirectOptions: {
      exclude: ['*'],
    }
  }
})