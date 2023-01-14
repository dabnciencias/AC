#!/usr/bin/env stack
-- stack runghc --package reanimate
{-# LANGUAGE OverloadedStrings #-}
module Main(main) where

import Codec.Picture (PixelRGBA8 (..))    -- Importamos una función que nos permite definir colores con código RGBA.
import Control.Lens  
import Control.Monad (forM_)              -- Importamos una función que nos permite iterar sobre listas.
import Reanimate                          -- API declarativo de Reanimate.
import Reanimate.Scene                    -- API imperativo de Reanimate; permite manipular objetos en la animación.

----------------------------------------------------------------------------------
-- Código principal de la animación, que fue generada usando reanimate-1.1.5.0. --
----------------------------------------------------------------------------------

main :: IO ()
main = reanimate $ addStatic (mkBackground "black") $ scene $ do

  cam <- newObject Camera -- Creamos una cámara

  -- Este bloque genera una lista con los objetos de texto (SVGs) que serán utilizados en la escena.
  
  texto <- mapM oNew [ curso, semestre ]

  -- Este bloque describe lo que sucederá en la escena con los objetos de texto.

  forM_ (zip texto posicionesY) $    -- Creamos un producto de las listas palabras y posicionesY (zip) e iteramos (forM_)
    \(obj, yPos) -> do                  -- sobre cada par ordenado del producto de las listas:
    oModify obj $ oCenterY .~ yPos      -- modificamos la posición vertical del objeto, 
    cameraAttach cam obj                -- usamos al objeto como referencia para la cámara, 
    cameraSetZoom cam 2.5                 -- fijamos la cámara tal que duplique el tamaño del objeto dee referencia
    oShowWith obj oDraw                 -- mostramos el objeto dibujándolo.

  forM_ texto $                         -- Iteramos sobre la lista de texto (forM_),
    \obj -> fork $ do                   -- escondiendo cada una de ellas con un "FadeOut".
    oHideWith obj oFadeOut              -- Realizamos la acción en paralelo para toda la lista (fork).

---------------------------------------------------------------------------------
----------------------------- Posiciones verticales. ----------------------------
---------------------------------------------------------------------------------

posicionesY :: [Double]
posicionesY = [ 0.5, -0.5 ]

----------------------------------------------------------------------------------
------- Aquí va el texto que escribiremos, renderizado como SVGs en LaTeX. -------
----------------------------------------------------------------------------------

curso :: SVG      
curso = withSubglyphs [0] (withStrokeColorPixel miNaranja) $ withSubglyphs [0] (withFillColorPixel miNaranja) $  withSubglyphs [1] (withStrokeColorPixel miVerde) $ withSubglyphs [1] (withFillColorPixel miVerde) $ withStrokeWidth 0 $ withFillOpacity 1 $ center $ scale 1.5 $
         latex "AC"


semestre :: SVG      
semestre = withSubglyphs [0..3] (withStrokeColorPixel miAzul) $ withSubglyphs [0..3] (withFillColorPixel miAzul) $  withSubglyphs [5,6] (withStrokeColorPixel miRojo) $ withSubglyphs [5,6] (withFillColorPixel miRojo) $ withStrokeWidth 0 $ withFillOpacity 1 $ withStrokeColor "white" $ withFillColor "white" $ center $
         latex "2023-II"

---------------------------------------------------------------------------------
----------------------- Colores definidos con código RGBA. ----------------------
---------------------------------------------------------------------------------

miAzul :: PixelRGBA8           
miAzul = PixelRGBA8 0 135 255 0    -- Color azul.

miRojo :: PixelRGBA8            
miRojo = PixelRGBA8 255 0 0 0      -- Color rojo.

miNaranja :: PixelRGBA8            
miNaranja = PixelRGBA8 255 119 0 0 -- Color naranja.

miVerde :: PixelRGBA8            
miVerde = PixelRGBA8 79 255 0 0    -- Color verde.
