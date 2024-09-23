<script setup lang="ts">
const client = useSupabaseClient()
const user = useSupabaseUser()
const logout = async () => {
  await client.auth.signOut()
  navigateTo('/')
}
</script>

<template>
  <main>
    
    <div class="grid grid-cols-12 gap-4">
      <div class="col-span-4 md:col-span-2 xl:col-span-1">
        <UAvatar size="3xl" :src="user.user_metadata.picture" alt="Avatar" />
      </div>
      <div class="col-span-8 md:col-span-10 xl:col-span-11 space-y-4">
        <UFormGroup label="Name">
          <UInput v-model="user.user_metadata.name" disabled size="xl" />
        </UFormGroup>
        <UFormGroup label="Email">
          <UInput v-model="user.email" disabled size="xl" />
        </UFormGroup>
        <UFormGroup label="Phone">
          <UInput v-model="user.phone" disabled size="xl" />
        </UFormGroup>
        <p>{{ user.id }}</p>
        <UButton @click="logout" color="white" icon="i-ic:baseline-logout" size="xl">Logout</UButton>
      </div>
    </div>
  </main>
</template>