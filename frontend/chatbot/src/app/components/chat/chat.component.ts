import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService } from '../../services/chat.service';
import { finalize } from 'rxjs/operators';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})
export class ChatComponent {
  userMessage = '';
  messages: { sender: string; text: string; matches?: any[] }[] = [];
  isLoading = false;

  constructor(
    private chatService: ChatService,
    private cdr: ChangeDetectorRef
  ) {}

  sendMessage() {
    const message = this.userMessage.trim();
    if (!message || this.isLoading) return;

    this.messages.push({ sender: 'user', text: message });
    this.userMessage = '';
    this.isLoading = true;

    this.cdr.detectChanges();

    this.chatService
      .sendMessage(message)
      .pipe(
        finalize(() => {
          this.isLoading = false;
          this.cdr.detectChanges();
        })
      )
      .subscribe({
        next: (res) => {
          this.messages.push({
            sender: 'bot',
            text: res.response,
            matches: res.matches || [],
          });
        },
        error: () => {
          this.messages.push({
            sender: 'bot',
            text: 'Error: Unable to connect to the server.',
          });
        },
      });
  }
}
