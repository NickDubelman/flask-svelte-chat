<script lang="ts">
  import type { Socket } from 'socket.io-client'

  export let socket: Socket
  export let user: string = ''

  let message = ''

  $: canSubmit = user.trim() !== '' && message.trim() !== ''

  function onSubmit() {
    socket.emit('message', { user, message }) // send message to server
    message = '' // clear message
  }
</script>

<form on:submit|preventDefault={onSubmit}>
  <input type="text" bind:value={message} placeholder="enter a message" />

  <button type="submit" disabled={!canSubmit}>Send</button>
</form>

<style>
  form {
    display: flex;
    justify-content: center;
  }

  input {
    width: 420px;
    outline: none;
  }

  button {
    cursor: pointer;
  }
</style>
