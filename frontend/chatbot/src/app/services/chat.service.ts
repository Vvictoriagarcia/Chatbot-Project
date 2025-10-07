import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  private apiUrl = 'http://127.0.0.1:5000/chat';

  private http = inject(HttpClient);

  sendMessage(message: string): Observable<{ response: string }> {
    return this.http.post<{ response: string }>(this.apiUrl, { message });
  }
}
