<script lang="ts">
  let message = ''

  function onSubmit() {
    alert('message sent!') // FIXME: send message to server
    message = '' // clear message
  }
</script>

<form on:submit|preventDefault={onSubmit}>
  <input type="text" bind:value={message} placeholder="enter a message" />

  <button type="submit" disabled={message.trim() === ''}>Send</button>
</form>

<style>
  form {
    display: flex;
    justify-content: center;
  }

  input {
    width: 420px;
  }

  button {
    cursor: pointer;
  }
</style>
