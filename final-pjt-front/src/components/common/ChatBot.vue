<template>
  <div class="chat-bot-container">
    <!-- 챗봇 버튼 -->
    <v-btn class="chat-bot-button" color="primary" icon elevation="4" size="large" @click="toggleChat">
      <v-icon>{{ isOpen ? 'mdi-close' : 'mdi-robot' }}</v-icon>
    </v-btn>

    <!-- 챗봇 대화창 -->
    <v-card v-show="isOpen" class="chat-window" width="350" elevation="8">
      <v-card-title class="d-flex align-center bg-primary">
        <span class="text-white">AI 금융 상담사</span>
        <v-spacer></v-spacer>
        <v-btn icon variant="text" @click="toggleChat">
          <v-icon color="white">mdi-close</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="chat-messages pa-4" ref="chatMessages">
        <div v-for="(message, index) in displayMessages" :key="index" :class="['message', message.role]">
          <v-card :color="message.role === 'assistant' ? 'grey-lighten-4' : 'primary'"
            :class="[message.role === 'assistant' ? '' : 'text-white', 'message-card']" class="mb-2 px-3 py-2"
            rounded="lg">
            {{ message.content }}
          </v-card>
        </div>
      </v-card-text>

      <v-card-actions class="pa-4 pt-0">
        <v-textarea 
          v-model.trim="userInput"
          placeholder="메시지를 입력하세요."
          variant="outlined"
          density="compact"
          hide-details
          @keyup.enter="sendMessage"
          auto-grow
          rows="1"
          no-resize
          class="chat-input">
          <template v-slot:append>
            <v-btn color="primary" icon variant="text" @click="sendMessage" :disabled="!userInput.trim()">
              <v-icon>mdi-send</v-icon>
            </v-btn>
          </template>
        </v-textarea>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import OpenAI from 'openai'
import { ref, watch, nextTick, computed } from 'vue' // Vue의 필수 기능들을 import

// 프롬프트 파일 import
import chatbotInstructions from '@/assets/prompts/chatbot-instructions.txt?raw'

const openai = new OpenAI({
  apiKey: import.meta.env.VITE_OPENAI_API_KEY,
  dangerouslyAllowBrowser: true
})

const isOpen = ref(false) // 챗봇 창의 열림/닫힘 상태를 관리하는 반응형 변수
const userInput = ref('') // 사용자 입력을 저장하는 반응형 변수
const messages = ref([
  {
    role: "system",
    content: chatbotInstructions
  },
  {
    role: "assistant",
    content: "안녕하세요! 서비스 관련 궁금하신 점이 있으시다면 무엇이든 물어보세요."
  }
])

// 채팅 메시지 창의 DOM 요소를 참조하기 위한 ref
const chatMessages = ref(null)

// computed 속성 추가
const displayMessages = computed(() => {
  return messages.value.filter(message => message.role !== 'system')
})

// 챗봇 창을 열고 닫는 토글 함수
const toggleChat = () => {
  isOpen.value = !isOpen.value
}

// 메시지 전송을 처리하는 비동기 함수
const sendMessage = async () => {
  const trimmedUserInput = userInput.value.trim()

  // 빈 메시지인 경우 전송하지 않음
  if (!trimmedUserInput) return

  // 사용자 메시지를 대화 내역에 추가
  messages.value.push({
    role: "user",
    content: trimmedUserInput
  })

  await callChatGPT()

  userInput.value = ''
}

// ChatGPT API를 호출 및 응답 처리
const callChatGPT = async () => {
  try {
    // API 호출하여 봇의 응답을 받아옴
    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: messages.value,
      temperature: 0.7,
      top_p: 1,
    });

    // console.log(response);

    // 봇의 응답을 대화 내역에 추가
    messages.value.push({
      role: "assistant",
      content: response.choices[0].message.content
    })
  } catch (error) {
    // 오류 발생 시 에러 메시지를 대화 내역에 추가
    messages.value.push({
      role: "assistant",
      content: '죄송합니다. 오류가 발생했습니다.'
    })
  }
}

// 메시지 배열이 변경될 때마다 실행되는 감시자
// 새 메시지가 추가될 때 스크롤을 자동으로 아래로 이동
watch(messages, async () => {
  // DOM 업데이트를 기다림
  await nextTick()
  // 채팅창이 존재하면 스크롤을 가장 아래로 이동
  if (chatMessages.value) {
    chatMessages.value.scrollTop = chatMessages.value.scrollHeight
  }
}, { deep: true }) // 깊은 감시 설정 (배열 내부 변화도 감지)
</script>

<style scoped>
.chat-bot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

.chat-bot-button {
  position: relative;
  z-index: 1001;
}

.chat-window {
  position: absolute;
  bottom: 80px;
  right: 0;
  height: 500px;
  display: flex;
  flex-direction: column;
}

.chat-messages {
  height: 380px;
  overflow-y: auto;
}

.message {
  margin-bottom: 8px;
  max-width: 80%;
  display: flex;
  flex-direction: column;
}

.message.user {
  margin-left: auto;
  align-items: flex-end;
}

.message.assistant {
  margin-right: auto;
  align-items: flex-start;
}

.message-card {
  display: inline-block;
  padding: 8px 12px;
  min-width: 60px;
  max-width: 100%;
  width: fit-content;
}

.chat-input :deep(.v-field__input) {
  min-height: 36px !important;
  padding-top: 5px !important;
}
</style>
