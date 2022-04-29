<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Tags;

class TagsPageController extends AbstractController
{
    /**
     * @Route("/tags_page/{id}", name="tags_page")
     */
    public function index(int $id): Response
    {

        $tag = $this->getDoctrine()->getRepository(Tags::class)->find($id);

        $tags = $this->getDoctrine()->getRepository(Tags::class)->findBy(['name' => $tag->getName()], ['id' => 'DESC']);

        return $this->render('tags_page/index.html.twig', [
            'tags' => $tags,
        ]);
    }
}
