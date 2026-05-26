import { Component, Input } from '@angular/core';
import { Product } from '../../../core/types/Products';

@Component({
  selector: 'app-products-card',
  imports: [],
  templateUrl: './products-card.component.html',
  styleUrl: './products-card.component.css'
})
export class ProductsCardComponent {
  @Input() product!:Product;

}
