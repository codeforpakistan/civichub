<script setup lang="ts">
const supabase = useSupabaseClient()

const signInWithOAuth = async () => {
  const { error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: 'http://localhost:3000/confirm',
    },
  })
  if (error) console.log(error)
}

const signOut = async () => {
  const { error } = await supabase.auth.signOut()
  if (error) console.log(error)
}
</script>

<template>
  <form class="min-h-screen row flex-center flex" @submit.prevent="signInWithOAuth">
    <div class="col-6 form-widget">
      <UButton
        label="Continue with Google"
        type="submit"
        color="primary" variant="solid"
      />
    </div>
  </form>
</template>