<template>
  <UContainer :ui="{ constrained: 'max-w-screen-2xl' }">
    <Navbar />
    <main class="my-8">
      <slot />
    </main>
    <Footer />
  </UContainer>
</template>
