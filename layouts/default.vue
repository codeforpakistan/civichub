<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <UDivider orientation="horizontal" />
    <div class="flex flex-grow">
      <div class="hidden md:flex">
        <Sidebar class="mb-2 p-4 min-w-48 md:min-w-48 lg:min-w-64" />
        <UDivider orientation="vertical" />
      </div>
      <UContainer :ui="{ base: '' }" class="py-4 sm:py-6 lg:py-8 items-start">
        <slot />
      </UContainer>
    </div>
  </div>
</template>
