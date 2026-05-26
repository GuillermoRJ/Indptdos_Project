import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchProductsComponent } from "./components/products/search-products/search-products.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, SearchProductsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'ecommerce-app';
}
